project('vita-parse-core')

py_mod = import('python')
py_executable = py_mod.find_installation('python3', required: true)

venv_dir = meson.current_build_dir() / '.venv'
run_command(py_executable, '-m', 'venv', venv_dir, check: true)
run_command(venv_dir / 'bin' / 'pip', 'install', '-r', meson.current_source_dir() / 'requirements.txt', check: true)

py_executable = py_mod.find_installation('python3', venv_dir: venv_dir)
