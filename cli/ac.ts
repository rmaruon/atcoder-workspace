const args = Array.from(Deno.args)
const subCommand = args.pop() || ''

const p = Deno.run({
  cmd: ['python', 'cli/main.py', subCommand, ...args],
  stdout: 'inherit',
  stderr: 'inherit',
})

const { code } = await p.status()

Deno.exit(code)
