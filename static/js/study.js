"use strict";

(() => {
  const subject = document.querySelector('.study-breadcrumb [data-pagefind-meta="subject"]');
  document.querySelectorAll('.sidebar-nav a').forEach(link => {
    if (link.href === window.location.origin + window.location.pathname) {
      link.setAttribute('aria-current', 'page');
    } else if (subject && link.href === subject.href) {
      link.setAttribute('aria-current', 'true');
    }
  });

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
  groups[0].table.parentNode.insertBefore(toolbar, groups[0].heading || groups[0].table);
  toolbar.hidden = false;
  toolbar.id = 'catalog-start';
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

  function filter() {
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
  }
  input.addEventListener('input', filter);
  select.addEventListener('change', filter);
  function resetFilter() {
    input.value = '';
    select.value = '';
    filter();
  }
  clear.addEventListener('click', () => {
    resetFilter();
    input.focus();
  });
  article.querySelectorAll('.intro-toc a[href]').forEach(link => {
    link.addEventListener('click', () => {
      const target = decodeURIComponent(new URL(link.href).hash.slice(1));
      if (groups.some(group => group.heading?.id === target && group.heading.hidden)) resetFilter();
    });
  });
  filter();
})();
