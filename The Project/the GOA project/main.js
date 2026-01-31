
const courses = [
    {
      title: "HTML & CSS Basics",
      description: "Learn the fundamentals of web development: HTML structure and CSS styling.",
      image: "Html.jpg",
      link: "#"
    },
    {
      title: "JavaScript Essentials",
      description: "Master core JavaScript concepts and DOM manipulation with hands-on projects.",
      image: "javaScript-Logo.jpg",
      link: "#"
    },
    {
      title: "React for Beginners",
      description: "Learn React basics and build interactive web applications.",
      image: "react.jpg",
      link: "#"
    }
  ];
  

  const projectsContainer = document.getElementById("projects-container");
  
  courses.forEach(course => {
    const card = document.createElement("div");
    card.classList.add("project-card");
    card.innerHTML = `
      <img src="${course.image}" alt="${course.title}">
      <h3>${course.title}</h3>
      <p>${course.description}</p>
    `;
    card.addEventListener("click", () => {
      window.open(course.link, "_blank");
    });
    projectsContainer.appendChild(card);
  });
  
  const contactForm = document.getElementById("contact-form");
  contactForm.addEventListener("submit", function(e){
    e.preventDefault();
    alert("Thank you for contacting Goal Academy!");
    contactForm.reset();
  });