// ===============================================
// Budget Alerts - Frontend helpers
// File: budget_project/static/alerts.js
// ===============================================

// Keep the slider label (e.g., "80%") in sync with the range input value.
(function () {
  const slider = document.getElementById('trigger');        // <input type="range" id="trigger" name="threshold_percent">
  const out = document.getElementById('triggerValue');      // <span id="triggerValue">...</span>

  if (!slider || !out) return;

  const update = () => {
    out.textContent = (slider.value || 0) + '%';
  };

  slider.addEventListener('input', update);
  update();
})();

// Lightweight client-side validation that mirrors your user stories.
// - Amount required
// - Category required
// Let Django handle all real validation and saving; we only block obvious empties.
(function () {
  const form = document.querySelector('form[method="post"]');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    const amount = document.getElementById('amountLimit');  // <input type="number" id="amountLimit" name="amount_limit">
    const category = document.getElementById('category');    // <select id="category" name="category">

    let ok = true;

    // Amount Required (must be > 0)
    if (!amount || !amount.value || Number(amount.value) <= 0) {
      if (amount) amount.classList.add('is-invalid');
      ok = false;
    } else {
      amount.classList.remove('is-invalid');
    }

    // Category Required (must have a value)
    if (!category || !category.value) {
      if (category) category.classList.add('is-invalid');
      ok = false;
    } else {
      category.classList.remove('is-invalid');
    }

    // If invalid, stop the submit. Otherwise, let Django handle it.
    if (!ok) {
      e.preventDefault();
      e.stopPropagation();
    }
  });
})();
