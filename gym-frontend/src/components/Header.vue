<template>
    <div class="">

    <!-- responsive navbar expand to vertically stack links on smaller screens -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

        <!-- Title / Logo -->
        <a class="navbar-brand" href="#">Gym Routine App</a>

        <!--button that appears on smaller screens (called navbar toggler) -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleDiv" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <!--toggler targets div collapse with targetted id-->
        <div class="collapse navbar-collapse" id="collapsibleDiv">
            <!-- navbar list-->
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0">

              <li class="nav-item">
                <a class="nav-link" href="#">Home<span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">My Workouts</a>
              </li>
            </ul>
            
            <!--
            {% if user.is_authenticated %}
                <span class="navbar-brand">Welcome {{user.title}} {{user.lname}}&emsp;<a href="{% url 'logout' %}">Logout</a></span>
            {%endif%}
            -->

      </div>

    </nav>
    </div>
</template>

<script>
export default {
    name: "Header",
}
</script>