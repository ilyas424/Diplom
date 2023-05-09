<template>
    <v-row justify="center">
        <v-dialog
                v-model="this.dialogwarning"
                persistent
                width="auto"
        >
            <template v-slot:activator="{ props }">

            </template>
            <v-card>
                <v-card-title class="text-h5">
                    <strong>Подтверждения</strong>
                </v-card-title>
                <v-card-text>Вы действительно хотите удалить?</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                   <slot></slot>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>
export default {
    props: {
        dialogwarning: false,
    },
    data () {
        return {

        }
    },
}
</script>