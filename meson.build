project('vita-parse-core')

py_mod = import('python')

venv_dir = meson.current_build_dir() / 'venv'

py_executable = py_mod.find_installation('python3',
  venv_dir: venv_dir,
  requirements: ['requirements.txt'],
  required: true
)
