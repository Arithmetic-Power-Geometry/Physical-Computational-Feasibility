# P01 GitHub binary upload method audit — 2026-11-07

## What is supported
GitHub connector has `create_blob` with `encoding=base64`, `create_tree`, `create_commit`, and `update_ref`. It can store binary files **if the caller can supply their Base64 content**. The authenticated repository is writable, as shown by prior commits.

## What is blocked
The supplied ZIP is mounted in the isolated local container (`/mnt/data/TAG_P01_Complete_Source_and_Build.zip`, 5.6 MiB); the GitHub connector runs in a different tool environment and has no file-path input, upload-by-URL endpoint, or direct access to local container bytes. The local container cannot resolve github.com, so `git push`/REST upload from it fails. The tools expose no safe binary-byte bridge from container files to the GitHub connector. Calling `create_blob` without the actual byte content would fabricate or corrupt the artifact.

## Integrity requirements
Do not mark P01 complete until original source/figures and revised manuscript are present at exact GitHub paths and their SHA256 hashes have been compared. A manifest or text status report does not replace the files.

## Supported manual completion route
The repository owner can extract the source package and upload the extracted folder contents via GitHub's Add file > Upload files, preserving relative paths in the extension, or use a local clone and `git add` / `git commit` / `git push`. Then the assistant can verify all uploaded paths and hashes via the connected GitHub tools. Do not commit the source archive's PDFs/build intermediates unnecessarily if repository size is a concern, but preserve the original ZIP in a release or original source archive if requested.
