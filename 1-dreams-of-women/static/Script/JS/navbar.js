//
const home_btn = document.getElementById('home');
home_btn.onclick = Home;
const About_btn = document.getElementById('About');
About_btn.onclick = About;


function Home() {
  $(function () {
      $("#maincontent").load("./importFiles/homecontent.html");
  });
};

function About() {
  $(function () {
      $("#maincontent").load("./importFiles/Aboutcontent.html");
  });
};