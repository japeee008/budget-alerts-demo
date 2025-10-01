// Slider label
(function () {
  const trigger = document.getElementById('trigger');
  const out = document.getElementById('triggerValue');
  if (trigger && out) {
    const update = () => (out.textContent = trigger.value + '%');
    trigger.addEventListener('input', update);
    update();
  }
})();

// Simple client-side validation (matches your user stories)
(function () {
  const form = document.getElementById('alertForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    const amount = document.getElementById('amountLimit');
    const category = document.getElementById('category');

    let ok = true;

    if (!amount.value || Number(amount.value) <= 0) {
      amount.classList.add('is-invalid');
      ok = false;
    } else {
      amount.classList.remove('is-invalid');
    }

    if (!category.value) {
      category.classList.add('is-invalid');
      ok = false;
    } else {
      category.classList.remove('is-invalid');
    }

    if (!ok) {
      e.preventDefault();
      e.stopPropagation();
      return;
    }

    // Prevent real submit for now (frontend mock)
    e.preventDefault();
    alert('Budget alert saved (frontend mock).');
  });
})();
