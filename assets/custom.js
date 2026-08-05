(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    document.addEventListener("click", function (e) {
      var toggle = e.target.closest("#side-nav-toggle");
      var nav = document.getElementById("side-nav");
      if (!nav) return;

      if (toggle) {
        e.preventDefault();
        e.stopPropagation();
        nav.classList.toggle("is-open");
        return;
      }
    });
  });
})();
