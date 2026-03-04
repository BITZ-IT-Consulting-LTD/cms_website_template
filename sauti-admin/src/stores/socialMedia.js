import { defineStore } from 'pinia'
import { api } from '@/utils/api'

export const useSocialMediaStore = defineStore('socialMedia', {
  state: () => ({
    posts: [],
    currentPost: null,
    loading: false,
    error: null
  }),

  getters: {
    activePosts: (state) => state.posts.filter(post => post.is_active),
    draftPosts: (state) => state.posts.filter(post => !post.is_active),

    postsByPlatform: (state) => (platform) => {
      return state.posts.filter(post => post.platform === platform)
    }
  },

  actions: {
    async fetchPosts(params = {}) {
      this.loading = true
      this.error = null

      try {
        const response = await api.socialMedia.list(params)
        this.posts = response.data.results || response.data || []
        return this.posts
      } catch (error) {
        this.error = error.message
        console.error('Failed to fetch social posts:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchPost(id) {
      this.loading = true
      this.error = null

      try {
        const response = await api.socialMedia.get(id)
        this.currentPost = response.data
        return this.currentPost
      } catch (error) {
        this.error = error.message
        console.error('Failed to fetch social post:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async createPost(postData) {
      this.loading = true
      this.error = null

      try {
        const response = await api.socialMedia.create(postData)
        this.posts.unshift(response.data)
        return response.data
      } catch (error) {
        this.error = error.message
        console.error('Failed to create social post:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async updatePost(id, postData) {
      this.loading = true
      this.error = null

      try {
        const response = await api.socialMedia.update(id, postData)
        const index = this.posts.findIndex(p => p.id === id)
        if (index !== -1) {
          this.posts[index] = response.data
        }
        return response.data
      } catch (error) {
        this.error = error.message
        console.error('Failed to update social post:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async deletePost(id) {
      this.loading = true
      this.error = null

      try {
        await api.socialMedia.delete(id)
        this.posts = this.posts.filter(p => p.id !== id)
      } catch (error) {
        this.error = error.message
        console.error('Failed to delete social post:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async toggleActive(id) {
      const post = this.posts.find(p => p.id === id)
      if (post) {
        return this.updatePost(id, { ...post, is_active: !post.is_active })
      }
    }
  }
})
