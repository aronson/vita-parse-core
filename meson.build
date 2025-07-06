project('vita-parse-core')

py_mod = import('python')
py_executable_system = py_mod.find_installation('python3', required: true)

venv_dir = meson.current_build_dir() / '.venv'
run_command(py_executable_system, '-m', 'venv', venv_dir, check: true)
run_command(venv_dir / 'bin' / 'pip', 'install', '-r', meson.current_source_dir() / 'requirements.txt', check: true)

py_executable = find_program(venv_dir / 'bin' / 'python3')
meson.override_variable('py_executable', py_executable)
