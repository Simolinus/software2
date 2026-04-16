const form = document.querySelector("#tv-form");
form.addEventListener("submit", async function (evt) {
  evt.preventDefault();
  const query = document.querySelector("input[name='q']").value;
  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${query}`,
    );
    const jsonData = await response.json();
    const div = document.getElementById("results");
    div.innerHTML = "";
    for (let i = 0; i < jsonData.length; i++) {
      console.log(jsonData[i]);
      const article = document.createElement("article");
      const title = document.createElement("h2");
      title.textContent = jsonData[i].show.name;
      const url = document.createElement("a");
      url.href = jsonData[i].show.url;
      url.target = "_blank";
      const image = document.createElement("img");
      image.alt = jsonData[i].show.name;
      if (jsonData[i].show.image === null) {
        image.src = "https://placehold.co/210x295?text=Not%20Found";
      } else {
        image.src = jsonData[i].show.image?.medium;
      }
      const summary = document.createElement("div");
      summary.innerHTML = jsonData[i].show.summary;
      article.appendChild(title);
      article.appendChild(url);
      article.appendChild(image);
      article.appendChild(summary);
      div.appendChild(article);
    }
  } catch (error) {
    console.error(error.message);
  }
});
