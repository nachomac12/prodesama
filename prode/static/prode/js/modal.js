var modal = document.getElementById('modal');
var elements = document.getElementsByClassName('toggle-modal');
for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', toggleClass);
}

function toggleClass() {
  modal.classList.toggle('is-active');
}
