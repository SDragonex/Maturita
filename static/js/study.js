"use strict";

// 1. Breadcrumb Subject Active State
(() => {
  const subject = document.querySelector('.study-breadcrumb [data-pagefind-meta="subject"]');
  document.querySelectorAll('.sidebar-nav a').forEach(link => {
    if (link.href === window.location.origin + window.location.pathname) {
      link.setAttribute('aria-current', 'page');
    } else if (subject && link.href === subject.href) {
      link.setAttribute('aria-current', 'true');
    }
  });
})();

// 2. Active Chapter Tracking (Scroll Spy)
(() => {
  const tocLinks = document.querySelectorAll('.right-rail .toc-links a, .inline-toc .toc-links a');
  if (!tocLinks.length) return;

  const headings = [];
  const linkMap = new Map();

  tocLinks.forEach(link => {
    try {
      const hash = new URL(link.href, window.location.href).hash;
      if (hash && hash.length > 1) {
        const id = decodeURIComponent(hash.slice(1));
        const el = document.getElementById(id);
        if (el) {
          if (!linkMap.has(el)) {
            headings.push(el);
            linkMap.set(el, []);
          }
          linkMap.get(el).push(link);
        }
      }
    } catch (_) {}
  });

  if (!headings.length) return;

  let activeEl = null;
  function setActive(targetEl) {
    if (activeEl === targetEl) return;
    activeEl = targetEl;
    tocLinks.forEach(link => {
      link.classList.remove('active');
      link.removeAttribute('aria-current');
    });
    if (targetEl && linkMap.has(targetEl)) {
      linkMap.get(targetEl).forEach(link => {
        link.classList.add('active');
        link.setAttribute('aria-current', 'location');
      });
    }
  }

  let ticking = false;
  function updateScrollSpy() {
    const offset = 120; // topbar height + comfortable offset
    const scrollPos = window.scrollY + offset;
    let current = null;
    for (let i = 0; i < headings.length; i++) {
      if (headings[i].offsetTop <= scrollPos) {
        current = headings[i];
      } else {
        break;
      }
    }
    setActive(current || headings[0]);
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateScrollSpy);
      ticking = true;
    }
  }, { passive: true });

  updateScrollSpy();
})();

// 3. Mobile Navigation Drawer Behavior
(() => {
  const sidebar = document.getElementById('sidebar');
  if (!sidebar) return;
  sidebar.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.matchMedia('(max-width: 960px)').matches && typeof window.toggleSidebar === 'function') {
        window.toggleSidebar(false);
      }
    });
  });
})();

// 4. Catalog Filtering (Literature and subject lists)
(() => {
  const toolbar = document.querySelector('[data-catalog-prefix]');
  if (!toolbar) return;
  const article = toolbar.closest('.article-content');
  const prefix = toolbar.dataset.catalogPrefix;
  const groups = [...article.querySelectorAll('table')].map(table => {
    const rows = [...table.querySelectorAll('tbody tr')].filter(row =>
      [...row.querySelectorAll('a[href]')].some(link => link.href.startsWith(prefix))
    );
    const previous = table.previousElementSibling;
    const next = table.nextElementSibling;
    return { table, rows,
      heading: previous && /^H[2-6]$/.test(previous.tagName) ? previous : null,
      separator: next?.tagName === 'HR' ? next : null
    };
  }).filter(group => group.rows.length);
  if (!groups.length) return;

  // Add .catalog-table to tables
  groups.forEach(group => group.table.classList.add('catalog-table'));

  // Split author and title in literature catalog for clear hierarchy
  if (prefix.includes('/cjl/')) {
    groups.forEach(group => {
      group.rows.forEach(row => {
        const link = row.querySelector('a');
        if (link && link.textContent.includes(': ') && !link.querySelector('.catalog-author')) {
          const parts = link.textContent.split(': ');
          link.innerHTML = `<span class="catalog-author">${parts[0]}:</span> <span class="catalog-title">${parts.slice(1).join(': ')}</span>`;
        }
      });
    });
  }

  // Identify first catalog heading
  const firstCatalogHeading = groups[0].heading || groups[0].table;

  // Find validity alert
  const validityAlert = article.querySelector('blockquote, aside.note');

  // Wrap methodology / criteria elements between validity alert and firstCatalogHeading into details.catalog-rules
  const methodologyElements = [];
  let curr = validityAlert ? validityAlert.nextElementSibling : article.firstElementChild;
  while (curr && curr !== firstCatalogHeading) {
    const next = curr.nextElementSibling;
    if (curr !== toolbar && !curr.classList.contains('article-intro-container') && !curr.classList.contains('study-breadcrumb')) {
      methodologyElements.push(curr);
    }
    curr = next;
  }

  if (methodologyElements.length > 0) {
    const details = document.createElement('details');
    details.className = 'catalog-rules';
    const summary = document.createElement('summary');
    summary.className = 'catalog-rules-summary';
    summary.innerHTML = '<i class="fa-solid fa-file-lines" aria-hidden="true"></i> Pravidla a podklady (kritéria výběru, PDF ke stažení)';
    details.appendChild(summary);

    const innerDiv = document.createElement('div');
    innerDiv.className = 'catalog-rules-content';
    methodologyElements.forEach(el => innerDiv.appendChild(el));
    details.appendChild(innerDiv);

    firstCatalogHeading.parentNode.insertBefore(details, firstCatalogHeading);
  }

  // Move toolbar to the top (right after validity alert or before catalog-rules)
  if (validityAlert && validityAlert.parentNode === article) {
    validityAlert.after(toolbar);
  } else {
    article.insertBefore(toolbar, article.querySelector('.catalog-rules') || firstCatalogHeading);
  }
  toolbar.hidden = false;
  toolbar.id = 'catalog-start';

  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('cs').trim();
  groups.forEach(group => {
    group.entries = group.rows.map(row => ({
      row,
      text: normalize(row.textContent),
      number: row.cells[0].textContent.trim()
    }));
  });
  const total = groups.reduce((sum, group) => sum + group.rows.length, 0);
  const input = toolbar.querySelector('input');
  const select = toolbar.querySelector('select');
  const status = toolbar.querySelector('[role="status"]');
  const clear = toolbar.querySelector('button');

  const jump = document.createElement('a');
  jump.href = '#catalog-start';
  jump.className = 'catalog-jump';
  jump.textContent = 'Přejít k seznamu ↓';
  article.querySelector('.intro-header .meta-line')?.appendChild(jump);

  if (groups.length > 1) {
    groups.forEach((group, index) => {
      const option = document.createElement('option');
      option.value = String(index);
      option.textContent = group.heading?.textContent.trim() || `Část ${index + 1}`;
      select.appendChild(option);
    });
    toolbar.querySelector('.catalog-category').hidden = false;
  }

  function syncURL(query, cat) {
    const params = new URLSearchParams(window.location.search);
    if (query) params.set('q', query);
    else params.delete('q');
    if (cat) params.set('cat', cat);
    else params.delete('cat');
    const qs = params.toString();
    const newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
    window.history.replaceState(null, '', newUrl);
  }

  function filter(updateHistory = true) {
    const query = normalize(input.value);
    const tokens = query.split(/\s+/).filter(Boolean);
    const byNumber = /^\d+$/.test(query) && groups.some(group =>
      group.entries.some(entry => Number(entry.number) === Number(query))
    );
    let count = 0;
    groups.forEach((group, index) => {
      let matches = 0;
      group.entries.forEach(({ row, text, number }) => {
        const visible = (select.value === '' || select.value === String(index)) &&
          (byNumber ? Number(number) === Number(query) : tokens.every(token => text.includes(token)));
        row.hidden = !visible;
        if (visible) matches++;
      });
      group.table.hidden = matches === 0;
      if (group.heading) group.heading.hidden = matches === 0;
      if (group.separator) group.separator.hidden = matches === 0;
      count += matches;
    });

    status.textContent = count ? `Zobrazeno ${count} z ${total}.` : 'Nic nenalezeno. Zkus jiný název, autora nebo zruš filtr.';
    clear.disabled = !input.value && !select.value;

    if (updateHistory) {
      syncURL(input.value.trim(), select.value);
    }
  }

  input.addEventListener('input', () => filter(true));
  select.addEventListener('change', () => filter(true));

  function resetFilter() {
    input.value = '';
    select.value = '';
    filter(true);
  }
  clear.addEventListener('click', () => {
    resetFilter();
    input.focus();
  });

  document.querySelectorAll('.intro-toc a[href], .right-rail a[href]').forEach(link => {
    link.addEventListener('click', () => {
      const target = decodeURIComponent(new URL(link.href).hash.slice(1));
      if (groups.some(group => group.heading?.id === target && group.heading.hidden)) {
        resetFilter();
      }
    });
  });

  // Read initial query params from URL
  const initialParams = new URLSearchParams(window.location.search);
  const initQ = initialParams.get('q');
  const initCat = initialParams.get('cat');
  if (initQ) input.value = initQ;
  if (initCat && select.querySelector(`option[value="${initCat}"]`)) {
    select.value = initCat;
  }

  // Handle browser back/forward history navigation
  window.addEventListener('popstate', () => {
    const p = new URLSearchParams(window.location.search);
    input.value = p.get('q') || '';
    select.value = p.get('cat') || '';
    filter(false);
  });

  window.addEventListener('pageshow', (event) => {
    if (event.persisted) {
      const p = new URLSearchParams(window.location.search);
      input.value = p.get('q') || '';
      select.value = p.get('cat') || '';
      filter(false);
    }
  });

  filter(false);
})();

// 5. Accessible Table Scroll Wrappers
(() => {
  document.querySelectorAll('.article-content table:not(.catalog-table)').forEach(table => {
    if (!table.parentElement.classList.contains('table-scroll')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-scroll';
      wrapper.setAttribute('role', 'region');
      const caption = table.querySelector('caption')?.textContent?.trim();
      wrapper.setAttribute('aria-label', caption ? `Tabulka: ${caption}` : 'Tabulka; při přesahu lze posouvat vodorovně');
      wrapper.tabIndex = 0;
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    }
  });
})();

// 6. Direct Print Mode Handling (Ctrl+P without dialog: expand all solutions, restore after print)
(() => {
  let printedDetails = [];
  window.addEventListener('beforeprint', () => {
    if (window.previousPrintState) return;
    printedDetails = [...document.querySelectorAll('.article-content details:not([open])')];
    printedDetails.forEach(item => item.open = true);
  });
  window.addEventListener('afterprint', () => {
    if (printedDetails.length) {
      printedDetails.forEach(item => item.open = false);
      printedDetails = [];
    }
  });
})();
