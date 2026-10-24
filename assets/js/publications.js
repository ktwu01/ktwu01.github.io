(() => {
  const root = document.querySelector('[data-publications]');
  if (!root) return;

  const form = root.querySelector('form');
  const query = form.elements.q;
  const type = form.elements.type;
  const year = form.elements.year;
  const topicButtons = [...form.querySelectorAll('[data-topic]')];
  const status = root.querySelector('[role="status"]');
  const empty = root.querySelector('.publication-empty');
  const sections = [...root.querySelectorAll('.publication-year')];
  const entries = [...root.querySelectorAll('[data-publication]')].map(element => ({
    element,
    topics: element.dataset.topics.split(' ').filter(Boolean),
    type: element.dataset.type,
    year: element.dataset.year,
    text: [...element.querySelectorAll('h3, .publication-venue, .publication-excerpt, .publication-tags, details p')]
      .map(part => part.textContent).join(' ').toLocaleLowerCase()
  }));
  let topic = '';

  function readLocation() {
    const params = new URLSearchParams(window.location.search);
    const requestedTopic = params.get('topic') || '';
    topic = topicButtons.some(button => button.dataset.topic === requestedTopic) ? requestedTopic : '';
    query.value = params.get('q') || '';
    type.value = params.get('type') || '';
    year.value = params.get('year') || '';
    // Unknown values should leave the corresponding filter unrestricted.
    if (type.selectedIndex < 0) type.value = '';
    if (year.selectedIndex < 0) year.value = '';
  }

  function writeLocation() {
    const url = new URL(window.location.href);
    const filters = { topic, q: query.value.trim(), type: type.value, year: year.value };
    Object.entries(filters).forEach(([key, value]) => {
      if (value) url.searchParams.set(key, value);
      else url.searchParams.delete(key);
    });
    // Filter results remain usable in browsers that restrict history updates.
    try { window.history.replaceState(null, '', url); } catch (_) { /* Keep local filters. */ }
  }

  function render(updateLocation = true) {
    const words = query.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const base = entries.filter(entry =>
      (!type.value || entry.type === type.value) &&
      (!year.value || entry.year === year.value) &&
      words.every(word => entry.text.includes(word))
    );
    const matches = new Set(base.filter(entry => !topic || entry.topics.includes(topic)));
    entries.forEach(entry => { entry.element.hidden = !matches.has(entry); });
    sections.forEach(section => {
      section.hidden = !section.querySelector('[data-publication]:not([hidden])');
    });
    topicButtons.forEach(button => {
      const id = button.dataset.topic;
      button.setAttribute('aria-pressed', String(id === topic));
      button.querySelector('[data-topic-count]').textContent = id ? base.filter(entry => entry.topics.includes(id)).length : base.length;
    });
    status.textContent = `${matches.size} of ${entries.length} publications`;
    empty.hidden = matches.size !== 0;
    if (updateLocation) writeLocation();
  }

  function clearFilters() {
    topic = '';
    query.value = '';
    type.value = '';
    year.value = '';
    render();
    form.querySelector('[type="reset"]').focus();
  }

  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', () => render());
  form.addEventListener('change', () => render());
  form.addEventListener('reset', event => {
    event.preventDefault();
    clearFilters();
  });
  root.addEventListener('click', event => {
    const button = event.target.closest('[data-topic]');
    const link = event.target.closest('[data-filter-topic]');
    if (button || (link && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey && event.button === 0)) {
      event.preventDefault();
      topic = button ? button.dataset.topic : link.dataset.filterTopic;
      render();
      if (link) {
        topicButtons.find(item => item.dataset.topic === topic).focus();
      }
    }
    if (event.target.closest('[data-clear-filters]')) clearFilters();
  });
  window.addEventListener('popstate', () => {
    readLocation();
    render(false);
  });

  readLocation();
  render(false);
  form.hidden = false;
  status.hidden = false;
})();
