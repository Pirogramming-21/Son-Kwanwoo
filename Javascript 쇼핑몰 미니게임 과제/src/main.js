// Fetch the itmes from the JSON file
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

// Main
loadItems()
    .then(items => {
        console.log(items);
})
.catch(console.log);