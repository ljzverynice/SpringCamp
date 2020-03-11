
var image1=document.getElementsByClassName('images1');
var image2=document.getElementsByClassName('images2');
var image3=document.getElementsByClassName('images3');
var button1=document.getElementsByClassName('button1');
var button2=document.getElementsByClassName('button2');
var button3=document.getElementsByClassName('button3');
var ad=document.getElementsByClassName("ad");
function change1(){
    image1[0].style.display="block";
    image2[0].style.display="none";
    image3[0].style.display="none";
    button1[0].style.backgroundColor="var(--yellow)";
    button2[0].style.backgroundColor="black";
    button3[0].style.backgroundColor="black";
    ad[0].innerHTML="RED DEAD ONLINE: MOONSHINERS";
}
function change2(){
    image2[0].style.display="block";
    image1[0].style.display="none";
    image3[0].style.display="none";
    button2[0].style.backgroundColor="var(--yellow)";
    button1[0].style.backgroundColor="black";
    button3[0].style.backgroundColor="black";
    ad[0].innerHTML="GRAND THEFT AUTO ONLINE: THE DIAMOND CASINO HEIST";
}
function change3(){
    image3[0].style.display="block";
    image2[0].style.display="none";
    image1[0].style.display="none";
    button3[0].style.backgroundColor="var(--yellow)";
    button2[0].style.backgroundColor="black";
    button1[0].style.backgroundColor="black";
    ad[0].innerHTML="RED DEAD REDEMPTION 2: PC LAUNCH TRAILER";
}
function getYellow(obj){
    obj.childNodes[3].childNodes[3].style.color="var(--yellow)";
}
function getBlack(obj){
    obj.childNodes[3].childNodes[3].style.color="black";
}
function raiseborder(obj){
    obj.style.backgroundColor="var(--yellow)";
}
function downborder(obj){
    obj.style.backgroundColor="white";
}