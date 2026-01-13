<template>
  <footer class="bg-[#006633] text-neutral-white py-20 font-sans">
    <div class="container-custom">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-12 lg:gap-8">
        <!-- Brand Column -->
        <div class="lg:col-span-4 space-y-8">
          <div>
            <h2 class="text-3xl font-black uppercase tracking-tight mb-4">Sauti 116</h2>
            <p class="text-neutral-white/70 font-bold leading-relaxed max-w-sm">
              Uganda's verified National Child Helpline. Providing 24/7 confidential support, guidance, and emergency intervention for all citizens.
            </p>
          </div>
          <div class="flex gap-4">
             <a href="https://facebook.com/Sauti116Helpline" target="_blank" class="w-12 h-12 rounded-full border border-neutral-white/20 flex items-center justify-center hover:bg-neutral-white hover:text-primary transition-all">
                <Facebook class="w-5 h-5" />
             </a>
             <a href="https://x.com/sauti116" target="_blank" class="w-12 h-12 rounded-full border border-neutral-white/20 flex items-center justify-center hover:bg-neutral-white hover:text-primary transition-all">
                <Twitter class="w-5 h-5" />
             </a>
             <a href="https://wa.me/256743889999" target="_blank" class="w-12 h-12 rounded-full border border-neutral-white/20 flex items-center justify-center hover:bg-neutral-white hover:text-primary transition-all">
                <MessageCircle class="w-5 h-5" />
             </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="lg:col-span-2 lg:col-start-6 space-y-8">
          <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50">Menu</h3>
          <ul class="space-y-4 font-bold">
            <li><router-link to="/" class="hover:text-secondary-light transition-colors">Home</router-link></li>
            <li><router-link to="/about" class="hover:text-secondary-light transition-colors">Who We Are</router-link></li>
            <li><router-link to="/videos" class="hover:text-secondary-light transition-colors">Videos</router-link></li>
            <li><router-link to="/blogs" class="hover:text-secondary-light transition-colors">Updates & Blogs</router-link></li>
            <li><router-link to="/resources" class="hover:text-secondary-light transition-colors">Resources</router-link></li>
          </ul>
        </div>

        <!-- Support -->
        <div class="lg:col-span-2 space-y-8">
          <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50">Support</h3>
          <ul class="space-y-4 font-bold">
            <li><router-link to="/report" class="hover:text-secondary-light transition-colors">Report a Case</router-link></li>
            <li><router-link to="/faqs" class="hover:text-secondary-light transition-colors">FAQs</router-link></li>
            <li><router-link to="/contact" class="hover:text-secondary-light transition-colors">Contact Us</router-link></li>
            <li><router-link to="/privacy" class="hover:text-secondary-light transition-colors">Privacy Policy</router-link></li>
            <li><router-link to="/terms" class="hover:text-secondary-light transition-colors">Terms of Service</router-link></li>
          </ul>
        </div>

        <!-- Contact Column -->
        <div class="lg:col-span-3 space-y-8">
           <h3 class="text-xs font-black uppercase tracking-widest text-neutral-white/50">Contact</h3>
           <div class="space-y-6">
              <a href="tel:116" class="flex items-center gap-4 group">
                 <div class="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all">
                    <Phone class="w-6 h-6" />
                 </div>
                 <div>
                    <span class="block text-xs font-bold opacity-60 uppercase tracking-wider">Toll Free</span>
                    <span class="text-2xl font-black">Call 116</span>
                 </div>
              </a>
              
              <a href="mailto:info@sauti116.ug" class="flex items-center gap-4 group">
                 <div class="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all">
                    <Mail class="w-6 h-6" />
                 </div>
                 <div>
                    <span class="block text-xs font-bold opacity-60 uppercase tracking-wider">Email Us</span>
                    <span class="text-lg font-bold">info@sauti116.ug</span>
                 </div>
              </a>
           </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="mt-20 pt-8 border-t border-neutral-white/10 flex flex-col md:flex-row items-center justify-between gap-6">
        <p class="text-xs font-bold text-neutral-white/40 uppercase tracking-widest">
           © 2026 Sauti 116. Ministry of Gender, Labour and Social Development.
        </p>
        <div class="flex items-center gap-2 text-neutral-white/40">
           <Globe class="w-4 h-4" />
           <span class="text-xs font-bold uppercase tracking-widest">Uganda</span>
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
