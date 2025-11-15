document.getElementById("btn").addEventListener("click", () => {
    console.log("Clicked!");
});
window.addEventListener("load", () => {
    console.log("Page fully loaded");
});
window.addEventListener("unload", () => {
    console.log("Page is unloading");
});
document.getElementById("textInput").addEventListener("change", () => {
    console.log("Value changed");
});
document.getElementById("box").addEventListener("mouseover", () => {
    console.log("Mouse entered box");
});
document.getElementById("box").addEventListener("mouseout", () => {
    console.log("Mouse left box");
});
document.getElementById("btn").addEventListener("mousedown", () => {
    console.log("Mouse button pressed down");
});
document.getElementById("btn").addEventListener("mouseup", () => {
    console.log("Mouse button released");
});

document.getElementById("textInput").addEventListener("blur", () => {
    console.log("Input lost focus");
});
document.getElementById("textInput").addEventListener("focus", () => {
    console.log("Input got focus");
});