<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">URC 2021</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <router-link class="nav-link" tag="a" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" tag="a" to="science-mission">Science Mission</router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Analysis</a>
      </li>
    </ul>
  </div>
</nav>
</template>
<style scoped>
.router-link-exact-active {
  color: rgba(0,0,0,.9)!important;
}
</style>