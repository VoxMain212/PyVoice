<template>
    <svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256" style="background: transparent;">
  <defs>
    <!-- Современный градиент в стиле 2023 года -->
    <linearGradient id="mainGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5865F2" />
      <stop offset="100%" stop-color="#43B581" />
    </linearGradient>
    
    <!-- Градиент для микрофона -->
    <linearGradient id="micGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F8F9FA" />
    </linearGradient>
    
    <!-- Градиент для анимации волн -->
    <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#43B581" />
      <stop offset="100%" stop-color="#5865F2" />
    </linearGradient>
  </defs>
  
  <!-- Фон с subtle текстурой -->
  <circle cx="128" cy="128" r="110" fill="#202225" />
  <circle cx="128" cy="128" r="100" fill="url(#mainGradient)" opacity="0.1" />
  
  <!-- Основной круг с эффектом глубины -->
  <circle cx="128" cy="128" r="90" fill="#2F3136" stroke="rgba(255,255,255,0.05)" stroke-width="2" />
  
  <!-- Стилизованный микрофон (минималистичный дизайн 2023) -->
  <path d="M128 70C145 70 158 83 158 100V140C158 157 145 170 128 170C111 170 98 157 98 140V100C98 83 111 70 128 70Z" 
        fill="url(#micGradient)" stroke="url(#mainGradient)" stroke-width="2" />
  

  <!-- Звуковые волны в современном flat-стиле -->
  <path d="M128 50C138 50 148 60 148 70V100C148 110 138 120 128 120C118 120 108 110 108 100V70C108 60 118 50 128 50Z" 
        fill="none" stroke="url(#waveGradient)" stroke-width="2" opacity="0.7" />
  
  <path d="M128 35C142 35 154 47 154 62V100C154 115 142 127 128 127C114 127 102 115 102 100V62C102 47 114 35 128 35Z" 
        fill="none" stroke="url(#waveGradient)" stroke-width="1.5" opacity="0.5" />
  
  <path d="M128 20C148 20 164 36 164 56V100C164 120 148 136 128 136C108 136 92 120 92 100V56C92 36 108 20 128 20Z" 
        fill="none" stroke="url(#waveGradient)" stroke-width="1" opacity="0.3" />

  <!-- Субтильные детали Python (стилизованная змея в фоновом узоре) -->
  <path d="M80 140Q95 150 100 160T110 180Q115 190 120 185T130 175Q140 170 150 165" 
        fill="none" stroke="url(#mainGradient)" stroke-width="0.5" opacity="0.15" />
</svg>
</template>