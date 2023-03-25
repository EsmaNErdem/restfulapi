// Creating Front-End to interact with API
const form = document.querySelector('#add-cc-form');
const flavorInput = form.querySelector('#flavor');
const sizeInput = form.querySelector('#size');
const ratingInput = form.querySelector('#rating');
const imageInput = form.querySelector('#image');
const ul = document.querySelector("#cc-list")
const deleteBtn = document.querySelectorAll("#delete-button")


// getting cupcakes list, return an array of cupcake objects.
async function getCupcakes(){
    const resp = await axios.get("/api/cupcakes");
    // console.log("---------", resp.data)
    return resp.data.cupcakes
}

function generateHtml(cupcake){
    let newCupcake = `
        <div data-cupcake-id=${cupcake.id}>
        <li>
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <button id="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
        src="${cupcake.image}"
        alt="(no image provided)">
        </div>
        `
    return newCupcake
}

document.addEventListener("DOMContentLoaded",  async () => {
    const cupcakes = await getCupcakes();
    for(let cupcake of cupcakes){
        let newCupcake =  generateHtml(cupcake)    
        ul.innerHTML += newCupcake
    }
});

// Adding event listener to submit form
form.addEventListener('submit', async function(event){
    event.preventDefault();
    const csrfToken = document.querySelector('#csrf_token').value;
    const flavor = flavorInput.value;
    const size = sizeInput.value;
    const rating = ratingInput.value;
    const image = imageInput.value;

    const resp = await axios.post(
        "/api/cupcakes", 
        {
            flavor,
            size,
            rating,
            image},
        {
            headers: {'X-CSRFToken': csrfToken}
        }
        
       )

    let new_cupcake = generateHtml(resp.data.cupcake)
    ul.innerHTML += new_cupcake

})


ul.addEventListener("click", async function(event){
    if(event.target.tagName === 'BUTTON'){
        let cupcake = event.target.closest("div");
        let id = cupcake.getAttribute('data-cupcake-id');
        const resp = await axios.delete(`/api/cupcakes/${id}`)
        console.log(resp)
        cupcake.remove()
    }

})


