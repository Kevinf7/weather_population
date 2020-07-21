export default {
  methods: {
    showError(error) {
      this.$buefy.notification.open({
        duration: 3000,
        message: error,
        position: 'is-bottom-right',
        type: 'is-danger',
        hasIcon: true
      })
    }
  }
}