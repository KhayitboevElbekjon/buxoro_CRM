const addBox = document.querySelector(".add-box"),
edit= document.querySelector(".edit"),
popupBox = document.querySelector(".popup-box"),
popupTitle = popupBox.querySelector("header p"),
closeIcon = popupBox.querySelector("header i"),
titleTag = popupBox.querySelector("input"),

ellipsis = document.querySelector(".fa-ellipsis"),
settings = document.querySelector(".settings");

havola =popupBox.querySelector(".havola")
descTag = popupBox.querySelector("input"),

addBtn = popupBox.querySelector("button");
console.log(ellipsis,settings,edit) ;
// const months = ["January", "February", "March", "April", "May", "June", "July",
//               "August", "September", "October", "November", "December"];
// const notes = JSON.parse(localStorage.getItem("notes") || "[]");
// let isUpdate = false, updateId;
addBox.addEventListener("click", () => {
    popupTitle.innerText = "Yangi mavzu qo'shish";
    addBtn.innerText =       "Kiritish";
    popupBox.classList.add("show");
 
    popupTitle.innerText =  "Yangi mavzu qo'shish";
    addBtn.innerText =  "Kiritish";
    popupBox.classList.add("show");
   
    document.querySelector("body").style.overflow = "hidden";
    if(window.innerWidth > 660) titleTag.focus();
});



closeIcon.addEventListener("click", () => {
    isUpdate = false;
    titleTag.value = descTag.value = ""; 
    popupBox.classList.remove("show");
    document.querySelector("body").style.overflow = "auto";
});

ellipsis.addEventListener("click",()=>{
    settings.classList.add("show")
})
edit.addEventListener("click", ()=>{
    addBox.click();
    settings.classList.remove("show")
} )

// function showNotes() {  
//     if(!notes) return;
//     document.querySelectorAll(".note").forEach(li => li.remove());
//     notes.forEach((note, id) => { 
//         let filterDesc = note.description.replaceAll("\n", '<br/>');
//         let liTag = `<li class="note">
//                         <div class="details">
//                             <p>${note.title}</p>
//                             <span>${filterDesc}</span>
//                             <a href='${note.Link}'><i class="fa-solid fa-paperclip"></i></a>
//                         </div>
//                         <div class="bottom-content">
//                             <span>${note.date}</span>
//                             <div class="settings">
//                                 <i onclick="showMenu(this)" class="fa-solid fa-ellipsis"></i>
//                                 <ul class="menu">
//                                     <li onclick="updateNote(${id}, '${note.title}', '${filterDesc}')"><i class="fa-solid fa-pen"></i>Edit</li>
//                                     <li onclick="deleteNote(${id})"><i class="fa-solid fa-trash-can"></i>Delete</li>
//                                 </ul>
//                             </div>
//                         </div>
//                     </li>`;
//         addBox.insertAdjacentHTML("afterend", liTag);
//     });
// }
// showNotes();

function showMenu(elem) {
    elem.parentElement.classList.add("show");
    document.addEventListener("click", e => {
        if(e.target.tagName != "I" || e.target != elem) {
            elem.parentElement.classList.remove("show");
        }
    });
}

// function deleteNote(noteId) {
//     let confirmDel = confirm("Are you sure you want to delete this note?");
//     if(!confirmDel) return;
//     notes.splice(noteId, 1);
//     // localStorage.setItem("notes", JSON.stringify(notes));
//     // showNotes();
// }
// function updateNote(noteId, title, filterDesc) {
//     // let description = filterDesc.replaceAll('<br/>', '\r\n');
//     // updateId = noteId;
//     isUpdate = true;
  
//     // titleTag.value = title;
//     // descTag.value = description;
//     // havola.value = Link;
//     // popupTitle.innerText = "Update a Note";
//     // addBtn.innerText = "Update Note";
// }    
 
// addBtn.addEventListener("click", e => {
//     e.preventDefault();
//     let title = titleTag.value.trim(),
//       Link=havola.value,
//     description = descTag.value.trim();

//     if(title || description || Link) {
//         let currentDate = new Date(),
//         month = months[currentDate.getMonth()],
//         day = currentDate.getDate(),
//         year = currentDate.getFullYear();

//         let noteInfo = {title,Link, description, date: `${month} ${day}, ${year}`}
//         // if(!isUpdate) {
//         //     notes.push(noteInfo);
//         // } else {
//         //     isUpdate = false;
//         //     notes[updateId] = noteInfo;
//         // }
//         // localStorage.setItem("notes", JSON.stringify(notes));
//         // showNotes();
//         // closeIcon.click(); 
//     }
// });