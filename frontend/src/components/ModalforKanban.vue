<template>
    <v-row justify="center">
        <v-dialog
                v-model="this.dialogchoise"
                scrollable
                width="auto"
        >
            <template v-slot:activator="{ props }">

            </template>
            <slot></slot>
        </v-dialog>
    </v-row>
</template>

<script>
export default {
    props:{
      dialogchoise: false
    },
    data () {
        return {
        }
    },
}
</script>