function sorpresa(){
  const links = [
    "https://www.therealzebos.com/goldenticket", 
    "https://milk.com",
    "https://searx.be",
    "https://www.youtube.com/watch?v=djD9fSSqXeA",
    "https://youtu.be/CkFeggecUiQ",
    "https://www.youtube.com/watch?v=AjnV0OtIM5g",
    "https://www.youtube.com/watch?v=EiESJHCcWRs&list=PLA0MyOqG7qq-He0VScSKU7CS7NPRNU4fJ"];
  var d = new Date();
  var day = d.getDay();
  window.open(links[day], "_blank");
}

