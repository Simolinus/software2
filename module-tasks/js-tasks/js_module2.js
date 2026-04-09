function task6() {
  const list = document.getElementById("list");
  while (true) {
    let li = document.createElement("li");
    let result = Math.floor(Math.random() * 6) + 1;
    li.textContent = result;
    list.appendChild(li);
    if (result === 6) {
      break;
    }
  }
}

function task10() {
  let candidates_list = [];
  let candidates_list_votes = [];

  const candidates = parseInt(prompt("Enter amount of candidates"));

  for (let i = 0; i < candidates; i++) {
    const candidate = prompt("Enter candidate name");
    candidates_list.push(candidate);
  }

  for (let i = 0; i < candidates_list.length; i++) {
    candidates_list_votes.push({ name: candidates_list[i], votes: 0 });
  }

  const voters = parseInt(prompt("Enter amount of voters"));

  for (let i = 0; i < voters; i++) {
    let vote_candidate = prompt("Enter candidate name you wish to vote for");
    for (let j = 0; j < candidates_list_votes.length; j++) {
      if (candidates_list_votes[j].name === vote_candidate) {
        candidates_list_votes[j].votes += 1;
      }
    }
  }
  let winner = candidates_list_votes[0];

  for (let j = 1; j < candidates_list_votes.length; j++) {
    if (candidates_list_votes[j].votes > winner.votes) {
      winner = candidates_list_votes[j];
    } else if (candidates_list_votes[j].votes === winner.votes) {
      winner = "No winner";
    }
  }

  if (winner === "No winner") {
    console.log(`No winner`);
  } else {
    console.log(`winner is ${winner.name} with ${winner.votes} votes.`);
  }
  console.log("results:");
  for (let j = 0; j < candidates_list_votes.length; j++) {
    console.log(
      `${candidates_list_votes[j].name}: ${candidates_list_votes[j].votes} votes`,
    );
  }
  return;
}
