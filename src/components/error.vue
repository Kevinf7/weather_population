<script>
  export default {
    danger() {
      const notif = this.$buefy.notification.open({
        duration: 5000,
        message: `Something's not good, also I'm on bottom`,
        position: 'is-bottom-right',
        type: 'is-danger',
        hasIcon: true
      })
    }
  }
</script>

