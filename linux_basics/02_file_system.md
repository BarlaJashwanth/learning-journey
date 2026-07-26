# Linux File System

## What is a File System?

A **File System** is the way Linux stores, organizes, and manages files and directories (folders).

Think of it like a cupboard:

```
Cupboard
 ├── Shelves
 │    ├── Folders
 │    │     ├── Files
```

Linux organizes everything in a **tree structure**, where every file and directory starts from a single location called the **Root Directory (`/`)**.

---

# Linux File System Structure

```
/
├── home
├── root
├── etc
├── bin
├── usr
├── var
├── tmp
└── ...
```

Every directory and file in Linux exists somewhere under the Root Directory.

---

# Root Directory (`/`)

The **Root Directory (`/`)** is the **top-most directory** in Linux.

It is the starting point of the entire Linux File System.

Every file, folder, application, and system directory is located under `/`.

## Key Points

- Top-most directory in Linux.
- Parent of all other directories.
- Starting point of the Linux File System.
- Shared by the entire operating system.
- Not a personal directory.

---

# Is `/` Personal for Each User?

**No.**

The Root Directory (`/`) is shared by:

- All users
- All applications
- The Linux operating system

Example:

```
/
├── home
│   ├── jashwanth
│   └── rahul
├── etc
├── root
└── var
```

There is only **one Root Directory** in the system.

---

# Important Linux Directories

## 1. `/home`

### Purpose

Stores the personal files and folders of normal users.

Every user gets their own directory inside `/home`.

Example:

```
/home
├── jashwanth
│   ├── Documents
│   ├── Downloads
│   └── project.py
├── rahul
└── priya
```

Example Path:

```
/home/jashwanth/Documents/notes.txt
```

Real-Life Analogy:

Imagine a hostel.

- `/home` = Hostel Building
- `jashwanth` = Room 101
- `rahul` = Room 102

Each user has their own personal space.

---

## 2. `/root`

### Purpose

`/root` is the **home directory of the Root User (Administrator)**.

> **Important:** `/` and `/root` are NOT the same.

Example:

```
/
├── root
│   ├── backup.sh
│   ├── server.conf
│   └── notes.txt
```

Only the Administrator (root user) normally uses this directory.

---

## 3. `/etc`

### Purpose

Stores **system configuration files**.

Linux and installed applications read these files while running.

Examples:

```
/etc
├── passwd
├── hosts
├── hostname
└── ssh/
```

Common Configuration Files:

- `/etc/passwd` → User account information
- `/etc/hosts` → Local hostname mappings
- `/etc/hostname` → Computer name
- `/etc/ssh/` → SSH configuration

Changing these files changes how the system behaves.

---

# Difference Between `/`, `/home`, `/root`, and `/etc`

| Directory | Purpose | Used By |
|-----------|----------|----------|
| `/` | Root Directory (starting point of Linux) | Entire Operating System |
| `/home` | Personal files of normal users | Normal Users |
| `/root` | Home directory of the Administrator | Root User |
| `/etc` | System configuration files | Linux & Applications |

---

# Example Linux Directory Tree

```
/
├── home
│   ├── jashwanth
│   └── rahul
├── root
├── etc
├── usr
├── bin
├── var
└── tmp
```
/root is the home directory of the root (administrator) user. Unlike normal users, the administrator has full privileges to manage the operating system, including installing software, modifying system files, managing users, and changing system configurations.

# ⚙️ `/etc` Directory

## 📌 What is `/etc`?

The **`/etc`** directory stores **system configuration files**.

It **does NOT** store your personal files. Instead, it stores settings that tell Linux **how the operating system and applications should behave**.

---

## 🎯 Purpose

- ⚙️ Stores system configuration files
- 👤 Stores user account information
- 🌐 Stores network configuration
- 🔒 Stores security and authentication settings
- 🚀 Stores service and startup configurations

---

# 👤 User Information

Linux stores user account information inside files like:

```text
/etc/passwd
/etc/shadow
```

### These files contain:

- 👤 Usernames
- 🆔 User IDs (UID)
- 🔒 Encrypted passwords (stored in `/etc/shadow`)

> **Example:** When you log in to Linux, the system checks these files to verify your account.

---

# 🌐 Network Configuration

Network settings are also stored inside `/etc`.

Example (Ubuntu):

```text
/etc/netplan/
```

It stores:

- 🌍 IP Address
- 🚪 Gateway
- 🌐 DNS Server
- 📡 Network Interface Settings

> **Example:** If you want to assign a static IP address, you usually edit files inside `/etc/netplan/`.

---

# 🔒 Service Configuration

Linux services store their configuration files inside `/etc`.

Example:

```text
/etc/ssh/sshd_config
```

This file controls:

- 🔑 SSH login settings
- 🔢 SSH Port Number
- 👑 Root login permission

> **Example:** If you want SSH to use port **2222** instead of **22**, you edit `sshd_config`.

---

# 🚀 System Startup & Services

Linux stores service-related configuration files inside:

```text
/etc/systemd/
```

These files control:

- 🚀 System startup
- 🔄 Background services
- ⚙️ Automatic service management

---

# 💡 Real-Life Analogy

Think of Linux as a **Car** 🚗

- `/home` → Your personal belongings 🧳
- `/root` → Car owner's private tools 🔑
- `/etc` → Car settings (engine, brakes, lights, steering) ⚙️

You don't keep luggage inside the engine.

Similarly, `/etc` stores **system settings**, not personal files.

---

# 📦 `/bin` Directory

## 📌 What is `/bin`?

The **`/bin`** directory contains **essential Linux commands (executables)** required for basic system operations.

Think of it as Linux's **toolbox** 🧰.

---

## 🎯 Purpose

- 🛠️ Stores basic Linux commands
- ⚡ Required for the operating system to function
- 💻 Used by both normal users and the administrator

---

# 🛠️ Common Commands Inside `/bin`

| Command | Purpose |
|---------|----------|
| `ls` | 📂 List files and folders |
| `cp` | 📋 Copy files |
| `mv` | 🚚 Move or rename files |
| `rm` | 🗑️ Remove files |
| `cat` | 📖 Display file contents |

---

# 💡 Example

When you type:

```bash
ls
```

Linux actually executes the program located at:

```text
/bin/ls
```

Similarly,

```bash
cp
```

runs

```text
/bin/cp
```

---

# 📂 Directory vs ⚡ Command

| 📂 Directory | ⚡ Command |
|-------------|------------|
| Stores files | Performs an action |
| Passive | Active |
| Example: `/home` | Example: `ls` |
| Just exists | You execute it |

---

# 💡 Real-Life Analogy

Imagine a **toolbox** 🧰

Inside it, you have:

- 🔨 Hammer
- 🔧 Screwdriver
- 🔩 Wrench

Similarly, `/bin` contains Linux's basic tools:

- 📂 `ls`
- 📋 `cp`
- 🚚 `mv`
- 🗑️ `rm`
- 📖 `cat`

Whenever you type a command, Linux picks the correct tool from `/bin`.

