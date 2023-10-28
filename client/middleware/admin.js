export default function ({store, redirect}) {
	if (!store.state.auth.loggedIn || !store.state.auth.user.rank.staff || !store.state.auth.user.rank.admin) {
		return redirect({ name: 'admin-login' });
	}
}
