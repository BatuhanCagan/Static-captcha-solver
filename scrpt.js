var a = document.createElement('a');
a.href = "img.png";
a.download = "output.png";
document.body.appendChild(a);
a.click();
document.body.removeChild(a);