const target = document.getElementById("target");
const li1 = document.createElement("li");
li1.textContent = "first item";
target.appendChild(li1);

const li2 = document.createElement("li");
li2.textContent = "second item";
target.appendChild(li2);

const li3 = document.createElement("li");
li3.textContent = "third item";
target.appendChild(li3);

li2.classList.add("my-item");

target.appendChild(li1);
target.appendChild(li2);
target.appendChild(li3);
