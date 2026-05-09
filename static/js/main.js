// Observatório de Projetos Integradores - JS

// Auto-remove flash messages after 5 seconds
document.querySelectorAll('.flash').forEach(flash => {
  setTimeout(() => {
    flash.style.opacity = '0';
    flash.style.transition = 'opacity 0.5s';
    setTimeout(() => flash.remove(), 500);
  }, 5000);
});
