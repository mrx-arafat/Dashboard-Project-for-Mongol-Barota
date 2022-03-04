export const routes = [
  {
    path: "/science-mission",
    name: "ScienceMission",
    component: () => import("./components/science/index.vue"),
},
{
  path: "/",
  name: "Home",
  component: () => import("./components/home/index.vue"),
},
]