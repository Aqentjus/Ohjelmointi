'use strict';


const names = ['John', 'Paul', 'Jones'];


let ul = document.getElementById("target");

names.forEach(name => {
  let li = document.createElement("li");
  li.textContent = name;
  ul.appendChild(li);
});
