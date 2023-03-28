<template>
  <div class="text-slate-800 font-mono min-h-screen h-full bg-slate-100 text-center">
    <div class="p-10 lg:w-9/12 xl:w-6/12 mx-auto">
      <p class="text-5xl">Lunch Menu Analysis</p>
      <div class="flex flex-row mt-10">
        <div class="flex flex-col w-6/12">
          <img v-if="image == 'menu'" src="~/assets/images/menu.jpg" class="rounded-xl rotate-[-12deg] transition ease-in-out hover:scale-110 hover:shadow-xl mt-10" >
          <img v-else-if="image == 'dog'" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftownsquare.media%2Fsite%2F40%2Ffiles%2F2017%2F03%2FDog-.jpg%3Fw%3D1200%26h%3D0%26zc%3D1%26s%3D0%26a%3Dt%26q%3D89&f=1&nofb=1&ipt=0bed59dc95a604b179d40f50fbdce71bd2e998da605eac60f1f0bdb831e9b532&ipo=images" class="rounded-xl rotate-[-12deg] transition ease-in-out hover:scale-110 hover:shadow-xl mt-10" >
        </div>
        <div class="flex flex-col w-6/12">
          <p>
            Most Common Words: <br />
            1. Seasonal: 123 <br />
            2. Vegetables: 108 <br />
            3. Salad: 93 <br />
            4. Rice: 76 <br />
            5. Chicken: 69 <br />
            6. Organic: 48 <br />
            7. Cheese: 45 <br />
            8. Veggie: 42 <br />
            9. Tofu: 32 <br />
            10. Beef: 29 <br />
            11. Housemade: 29 <br />
            12. Roasted: 27 <br />
            13. Soup: 26 <br />
            14. Pasta: 25 <br />
            15. Niman: 23 <br />
            16. Ranch: 23 <br />
            17. Marinara: 20 <br />
            <a @click="image = 'dog'">18. Dogs: 20 </a><br />
            19. Pizza: 20 <br />
            20. Sauce: 19 <br />
            21. Kale: 18 <br />
            22. Vegetable: 18 <br />
            23. Quesadillas: 17 <br />
            24. Bread: 17 <br />
            25. Bean: 16 <br />
          </p>
        </div>
      </div>
      <div class="flex flex-row mt-10">
        <div class="flex flex-col w-6/12">
          Most Common Nouns: <br />
          1. Vegetables: 108 <br />
          2. Salad: 93 <br />
          3. Rice: 76 <br />
          4. Chicken: 69 <br />
          5. Cheese: 45 <br />
          6. Veggie: 42 <br />
          7. Tofu: 32 <br />
          8. Beef: 29 <br />
          9. Soup: 26 <br />
          10. Pasta: 25 <br />
          11. Dogs: 20 <br />
          12. Pizza: 20 <br />
          13. Kale: 18 <br />
          14. Vegetable: 18 <br />
          15. Quesadillas: 17 <br />
          16. Bread: 17 <br />
          17. Bean: 16 <br />
          18. Beans: 15 <br />
          19. Coconut: 15 <br />
          20. Potato: 14 <br />
          21. Sandwich: 14 <br />
          22. Greens: 13 <br />
          23. Cauliflower: 13 <br />
          24. Curry: 12 <br />
          25. Burgers: 11 <br />
        </div>
        <div class="flex flex-col w-6/12">
          Most Common Adjectives: <br />
          1. Seasonal: 123 <br />
          2. Organic: 48 <br />
          3. Housemade: 29 <br />
          4. Roasted: 27 <br />
          5. Niman Ranch: 23 <br />
          6. Baked: 15 <br />
          7. Smoky: 15 <br />
          8. Springer: 14 <br />
          9. Hodo: 14 <br />
          10. Sweet: 13 <br />
          11. Brown: 13 <br />
          12. Mountain: 12 <br />
          13. Penne: 11 <br />
          14. Whole: 10 <br />
          15. Hot: 10 <br />
          16. Local: 10 <br />
          17. Glazed: 9 <br />
          18. Sautéed: 9 <br />
          19. Zoe's: 9 <br />
        </div>
      </div>
      <div class="pt-10">
        Created by <a href="https://www.lucaskchang.com" target="_blank" class="text-blue-500 hover:text-blue-700">Lucas Chang</a>. Made with Nuxt.js and Tailwind CSS.
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
const image = ref("menu")
</script>