<template>
      <v-container>
          <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-indicators">
                  <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                  <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
                  <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
              </div>
              <div class="carousel-inner">
                  <div class="carousel-item active">
                      <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

                      <div class="container">
                          <div class="carousel-caption text-start">
                              <h1>Cedar.</h1>
                              <p>программный продукт, созданный специально, что бы управлять проектами.</p>
                          </div>
                      </div>
                  </div>
                  <div class="carousel-item">
                      <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

                      <div class="container">
                          <div class="carousel-caption">
                              <h1>Лицензирование и оплата.</h1>
                              <p>Покупка Cedar доступна в 3 видах оплаты: одноразовый и ежемесячный платеж, а также годовая подписка.</p>
                          </div>
                      </div>
                  </div>
                  <div class="carousel-item">
                      <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

                      <div class="container">
                          <div class="carousel-caption text-end">
                              <h1>Гибкое управления проектами.</h1>
                              <p>Cedar построен на основе скрещивания современных подходов Scrum и Kanban.</p>
                          </div>
                      </div>
                  </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
              </button>
          </div>
      </v-container>
</template>

<script>
export default {
    name: "myCarousel"
}
</script>

<style scoped>

</style>