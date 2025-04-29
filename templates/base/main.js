// Header Scroll color change

let header=document.querySelector('header');

window.addEventListener('scroll',()=>{
    header.classList.toggle('shadow',window.scrollY >0)
})

   {% comment %} <!-- Bootstrap4 files-->
    <script src="{% static 'js/bootstrap.bundle.min.js' %}" type="text/javascript"></script>
    <link href="{% static 'css/bootstrap.css' %}" rel="stylesheet" type="text/css"/>
    
    <!-- Font awesome 5 -->
    <link href="{% static 'fonts/fontawesome/css/all.min.css' %}" type="text/css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <!-- custom style -->
    <link href="{% static 'css/ui.css' %}" rel="stylesheet" type="text/css"/>
    <link href="{% static 'css/responsive.css' %}" rel="stylesheet" media="only screen and (max-width: 1200px)" />
    
    <link href="{% static 'css/custom.css' %}" rel="stylesheet" type="text/css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
     {% endcomment %}
{% comment %} <!-- custom javascript -->
<script src="{% static 'js/script.js' %}" type="text/javascript"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="{% static 'js/jquery-3.3.1.min.js' %}" type="text/javascript"></script>
<script src="https://static.elfsight.com/platform/platform.js" async></script> {% endcomment %}

{% comment %} <!-- Bootstrap JS and Popper.js (for dropdown) -->
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  {% endcomment %}

  
.footer-section {
    padding: 40px 0;
    background-color: #000;
    color: white;
  }
  
  .footer-link {
    color: #bbb;
    text-decoration: none;
    transition: color 0.3s ease-in-out;
  }
  .footer-link:hover {
    color: var(--main-light-color);;
  }
  
  /* Social Media Icons */
  .social-icon {
    color: #bbb;
    font-size: 1.5rem;
    transition: color 0.3s ease-in-out;
  }
  .social-icon:hover {
    color: var(--main-light-color);;
  }
  /* Newsletter Form */
  .newsletter-form {
    max-width: 100%;
  }
  
  .newsletter-form .input-group {
    display: flex;
    align-items: center;
    width: 100%;
  }
  
  .newsletter-form .form-control {
    height: 45px; /* Fixed height */
    border-radius: 5px 0 0 5px;
    border: 1px solid #ddd;
    font-size: 1rem;
    padding: 10px;
    flex-grow: 1; /* Ensures input takes available space */
  }
  
  .newsletter-form .btn {
    height: 45px; /* Matches input height */
    border-radius: 0 5px 5px 0;
    font-size: 1rem;
    padding: 10px 15px;
    white-space: nowrap; /* Prevents button from wrapping */
  }
  
  /* Newsletter Form */
.newsletter-form {
  max-width: 100%;
}

.newsletter-form .input-group {
  display: flex;
  align-items: center;
  width: 100%;
}

.newsletter-form .form-control {
  height: 45px; /* Fixed height */
  border-radius: 5px 0 0 5px;
  border: 1px solid #ddd;
  font-size: 1rem;
  padding: 10px;
  flex-grow: 1; /* Ensures input takes available space */
}

.newsletter-form .btn {
  height: 45px; /* Matches input height */
  border-radius: 0 5px 5px 0;
  font-size: 1rem;
  padding: 10px 15px;
  white-space: nowrap; /* Prevents button from wrapping */
}