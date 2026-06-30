# How to Run and Test the Directory Daemon Locally

If you want to test the `dirctl` daemon right now, you have a few easy options depending on whether you want to compile the code, run it directly with Go, or use Docker.

Since you are already inside the project's source code directory, choose one of the following methods:

---

## Method 1: The Quickest Way (using `go run`)
You don't even need to compile a binary to test the daemon. You can use Go to directly execute the CLI module's code in memory.

1. Ensure you are at the root of the project (`/Users/sumanjeet/code/dir`).
2. Run the following command:
   ```bash
   cd cli
   go run . daemon start
   ```
*This will immediately start the Directory Node. It will create its local state in `~/.agntcy/dir/` and begin listening on `localhost:8888`.*

---

## Method 2: Compile the Binary (using `Taskfile`)
If you want to build the actual `dirctl` executable (just like it would be in production), you can use the project's `Taskfile` system.

1. Ensure dependencies are fetched (optional but recommended):
   ```bash
   task deps
   ```
2. Compile the CLI binary:
   ```bash
   task cli:compile
   ```
3. The binary will be output to a hidden `.bin` directory at the project root. Run it using:
   ```bash
   ./.bin/dirctl daemon start
   ```

---

## Method 3: Using Docker Compose
If you prefer not to touch your local Go installation and want the full stack (including PostgreSQL and Zot registry), use Docker.

1. Navigate to the docker install directory:
   ```bash
   cd install/docker
   ```
2. Start the services in the background:
   ```bash
   docker compose up -d
   ```
3. To view the logs and see what the daemon is doing:
   ```bash
   docker compose logs -f apiserver
   ```

---

### How to verify it is running?
Once you have started the daemon using **Method 1** or **Method 2**, open a new terminal window and use the `status` command to check on it:

```bash
# If using the compiled binary
./.bin/dirctl daemon status

# Or if using go run
cd cli && go run . daemon status
```

You should see output indicating that the node is healthy, the Kademlia DHT is active, and the gRPC API is listening!
