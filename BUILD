python_distribution(
    name="toolA-cli",
    entry_points={
       "console_scripts": {"acli": "toolA.cli.main:cli"},
    },
    dependencies=[
        # Dependencies on code to be packaged into the distribution.
    ],
    provides=python_artifact(
        name="toolA-mycli",
        version="0.1.0",
        description="My CLI ToolA Sample",
        author="Roberto Barbosa, rnrbarbosa@gmail.com",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    ),
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
)

python_distribution(
    name="toolB-cli",
    entry_points={
       "console_scripts": {"bcli": "toolB.cli.main:cli"},
    },
    dependencies=[
        # Dependencies on code to be packaged into the distribution.
    ],
    provides=python_artifact(
        name="toolB-cli",
        version="0.1.0",
        description="My CLI ToolB Sample",
        author="Roberto Barbosa, rnrbarbosa@gmail.com",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    ),
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
)