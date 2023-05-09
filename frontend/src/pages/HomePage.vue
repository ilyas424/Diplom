<template>
        <div>
            <section class="py-5 text-center container">
                <div class="row py-lg-5">
                    <div class="col-lg-6 col-md-8 mx-auto">
                        <h1 class="fw-light">Cedar</h1>
                        <p class="lead text-muted">Для доступа к основным возможностям системы Cedar требуется войти или зарегистрироваться </p>
                            <div>
                            <a @click="$router.push('/auth')"  class="btn btn-outline-secondary my-2">Войти</a>
                            </div>
                            <div>
                            <a @click="$router.push('/registration')"  class="btn btn-secondary my-2">Зарегистрироваться</a>
                            </div>
                    </div>
                </div>
            </section>
        </div>
</template>

<script>
export default {
    name: "HomePage"
}
</script>

<style scoped>

.btn{
    padding: 10px;
}

</style>