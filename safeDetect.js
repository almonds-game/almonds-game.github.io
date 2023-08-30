var ipAddr = fetch("https://api.ipify.org/?format=json")
  .then(results => results.json());

console.log(results.ip);
