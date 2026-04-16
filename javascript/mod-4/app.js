const form = document.getElementById('searchForm');
const input = document.getElementById('searchInput');
const results = document.getElementById('results');

form.addEventListener('submit', function (event) {
  event.preventDefault();

  const query = input.value.trim();

  if (!query) return;

  fetch(`https://api.chucknorris.io/jokes/search?query=${query}`)
    .then(response => response.json())
    .then(data => {
      results.innerHTML = '';

      data.result.forEach(joke => {
        const article = document.createElement('article');
        const p = document.createElement('p');

        p.textContent = joke.value;

        article.appendChild(p);
        results.appendChild(article);
      });
    })
    .catch(error => {
      console.error('Error fetching jokes:', error);
    });
});
