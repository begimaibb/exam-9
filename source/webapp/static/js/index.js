// async function getTagArticles(event) {
//     event.preventDefault()
//     let target = event.target;
//     let tagId = target.dataset.tagId;
//     console.log(tagId)
//     let url = target.dataset.url;
//     let response = await fetch(`${url}?tag_id=${tagId}`);
//     if (response.ok){
//         let photos = await response.json()
//
//
//         let caption = document.getElementById("caption");
//         caption.innerHTML = "";
//         for (let i = 0; i < photos.length; i++) {
//             let div = document.createElement("div")
//             let photo_caption = document.createElement("p")
//             photo_caption.innerText = photos[i].content
//             div.appendChild(photo_caption)
//             caption.appendChild(div)
//     }}
//
// }
//
// async function sendSearchValue(event){
//     event.preventDefault()
//     let target = event.target
//     let input = target.querySelector('[name="search"]')
//     console.log(input.value)
//
//     console.log(input)
//
// }
//
// async function sendFavorite(event){
//     event.preventDefault();
//     let target = event.target;
//     let url = target.href;
//     let response = await fetch(url);
//     let response_json = await response.json();
//     let count = response_json.count;
//     console.log(count);
//     let photoId = target.dataset.photoId;
//     let span = document.getElementById(photoId);
//     span.innerText = `Favorites: ${count}`;
//     if(target.innerText === "Non-favourite"){
//         target.innerText = "Favorite";
//     }
//     else{
//         target.innerText = "Non-favourite";
//     }
// }
//
//
// function onloadFunc() {
//     let tags = document.getElementsByClassName("tag");
//     console.log(tags)
//     for (let i = 0; i < tags.length; i++) {
//         tags[i].addEventListener("click", getTagArticles)
//     }
//
//     let form = document.getElementById("search_id")
//     if (form){
//         form.addEventListener("submit", sendSearchValue)
//     }
//
//
//     let likes = document.getElementsByClassName("likes");
//     for (let i = 0; i < likes.length; i++) {
//         likes[i].addEventListener("click", sendLike)
//     }
// }
//
// window.addEventListener("load", onloadFunc)