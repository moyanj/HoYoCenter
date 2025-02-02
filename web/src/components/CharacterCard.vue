<script setup lang="ts">
import { get_sr_character_info, get_ys_character_info } from "@/api/res";
import { ref, watch } from "vue";
import { ElCard } from "element-plus";

const props = defineProps<{
    character: number,
    game: string
}>()

var src = ref("");

watch(props, (newValue, oldValue) => {
    if (props.game == "sr") {
        src.value = `/resources/StarRail/CharacterIcon/${props.character}.png`
    } else {
        src.value = `/resources/Genshin/AvatarIcon/${props.character}.png`
    }
}, {
    immediate: true
})

</script>

<template>
    <el-card>
        <img :src="src" />
    </el-card>
</template>

<style scoped>
.el-card {
    --el-card-padding: 1px;

}

.el-card img {
    width: 100%;
    height: 100%;
}
</style>