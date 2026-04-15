const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

trigger.addEventListener('mouseenter', () => {
  target.src = 'img/picb.jpg';
})

trigger.addEventListener('mouseleave', () => {
  target.src = 'img/pica.jpg';
})








