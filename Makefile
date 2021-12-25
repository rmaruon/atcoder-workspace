install:
	deno compile --allow-run cli/ac.ts
	@mv ac ~/.bin/

uninstall:
	@rm ~/.bin/ac
