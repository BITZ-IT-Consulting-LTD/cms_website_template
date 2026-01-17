<template>
  <footer class="bg-[#006633] text-neutral-white py-20" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
    <div class="container-custom">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-12 lg:gap-8">
        <!-- Brand Column -->
        <div class="lg:col-span-4 space-y-8">
          <div>
            <h2 class="text-3xl font-black uppercase tracking-tight mb-4" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Sauti 116</h2>
            <p class="text-neutral-white/70 font-bold leading-relaxed max-w-sm" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              Uganda's verified National Child Helpline. Providing 24/7 confidential support, guidance, and emergency intervention for all citizens.
            </p>
          </div>
          <div class="flex gap-4">
             <!-- X (Twitter) -->
             <a href="https://x.com/sauti116" target="_blank" class="social-btn group relative w-12 h-12 rounded-full bg-transparent flex items-center justify-center transition-all hover:scale-110">
                <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path>
                </svg>
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">X</span>
             </a>
             <!-- Instagram -->
             <a href="https://instagram.com/sauti116" target="_blank" class="social-btn group relative w-12 h-12 rounded-full bg-transparent flex items-center justify-center transition-all hover:scale-110">
                <svg class="w-7 h-7 text-[#E1306C] fill-current" viewBox="0 0 24 24" aria-hidden="true">
                   <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Instagram</span>
             </a>
             <!-- Facebook -->
             <a href="https://facebook.com/Sauti116Helpline" target="_blank" class="social-btn group relative w-12 h-12 rounded-full bg-transparent flex items-center justify-center transition-all hover:scale-110">
                <svg class="w-8 h-8 text-[#1877F2] fill-current" viewBox="0 0 24 24" aria-hidden="true">
                   <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                </svg>
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Facebook</span>
             </a>
             <!-- TikTok -->
             <a href="https://tiktok.com/@sauti116" target="_blank" class="social-btn group relative w-12 h-12 rounded-full bg-transparent flex items-center justify-center transition-all hover:scale-110">
                <svg class="w-7 h-7 text-white fill-current" viewBox="0 0 24 24" aria-hidden="true">
                   <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/>
                </svg>
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">TikTok</span>
             </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="lg:col-span-2 lg:col-start-6 space-y-8">
          <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Menu</h3>
          <ul class="space-y-4 font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
            <li><router-link to="/" class="hover:text-secondary-light transition-colors">Home</router-link></li>
            <li><router-link to="/about" class="hover:text-secondary-light transition-colors">Who We Are</router-link></li>
            <li><router-link to="/videos" class="hover:text-secondary-light transition-colors">Videos</router-link></li>
            <li><router-link to="/blogs" class="hover:text-secondary-light transition-colors">Updates</router-link></li>
            <li><router-link to="/news" class="hover:text-secondary-light transition-colors">Blogs</router-link></li>
            <li><router-link to="/resources" class="hover:text-secondary-light transition-colors">Resources</router-link></li>
          </ul>
        </div>

        <!-- Support -->
        <div class="lg:col-span-2 space-y-8">
          <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Support</h3>
          <ul class="space-y-4 font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
            <li><router-link to="/report" class="hover:text-secondary-light transition-colors">Report a Case</router-link></li>
            <li><router-link to="/faqs" class="hover:text-secondary-light transition-colors">FAQs</router-link></li>
            <li><router-link to="/contact" class="hover:text-secondary-light transition-colors">Contact Us</router-link></li>
            <li><router-link to="/privacy" class="hover:text-secondary-light transition-colors">Privacy Policy</router-link></li>
            <li><router-link to="/terms" class="hover:text-secondary-light transition-colors">Terms of Service</router-link></li>
          </ul>
        </div>

        <!-- Contact Column -->
        <div class="lg:col-span-3 space-y-8">
           <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Contact</h3>
           <div class="space-y-6">
              <a href="tel:116" class="flex items-center gap-4 group">
                 <div class="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all">
                    <Phone class="w-6 h-6" />
                 </div>
                 <div>
                    <span class="block text-xs font-bold opacity-60 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Toll Free</span>
                    <span class="text-2xl font-black" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Call 116</span>
                 </div>
              </a>
              
              <a href="mailto:info@sauti116.ug" class="flex items-center gap-4 group">
                 <div class="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all">
                    <Mail class="w-6 h-6" />
                 </div>
                 <div>
                    <span class="block text-xs font-bold opacity-60 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Email Us</span>
                    <span class="text-lg font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">info@sauti116.ug</span>
                 </div>
              </a>
           </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="mt-20 pt-8 border-t border-neutral-white/10 flex flex-col md:flex-row items-center justify-between gap-6">
        <p class="text-xs font-bold text-neutral-white/40 uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
           © 2026 Sauti 116. Ministry of Gender, Labour and Social Development.
        </p>
        <div class="flex items-center gap-2 text-neutral-white/40">
           <Globe class="w-4 h-4" />
           <span class="text-xs font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Uganda</span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { 
  Phone, 
  Mail, 
  Facebook, 
  Twitter, 
  MessageCircle, 
  Globe 
} from 'lucide-vue-next'
</script>

<style scoped>
.social-tooltip {
  position: absolute;
  bottom: 110%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background-color: #FFFFFF;
  color: #000000;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 700;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  pointer-events: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
  font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;
}

/* Tooltip Arrow */
.social-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -6px;
  border-width: 6px;
  border-style: solid;
  border-color: #FFFFFF transparent transparent transparent;
}

/* Reveal Tooltip on Hover */
.group:hover .social-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}
</style>
