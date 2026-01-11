// Initialize CodeMirror editors for Python textareas (#code and #prompt)
(function() {
  function createEditor(textareaId) {
    const ta = document.getElementById(textareaId);
    if (!ta) return null;
    // pick theme based on page theme attribute
    const pageTheme = document.documentElement.getAttribute('data-theme') || '';
    const themeName = pageTheme === 'dark' ? 'darcula' : 'default';
    const editor = CodeMirror.fromTextArea(ta, {
      mode: 'python',
      lineNumbers: true,
      matchBrackets: true,
      autoCloseBrackets: true,
      indentUnit: 4,
      indentWithTabs: false,
      theme: themeName,
      extraKeys: {
        'Ctrl-/': 'toggleComment',
        'Cmd-/': 'toggleComment',
        'Tab': function(cm) { if (cm.somethingSelected()) cm.indentSelection('add'); else cm.replaceSelection('  ', 'end'); }
      }
    });
    // Sync value back to textarea on change
    editor.on('change', function(cm) {
      ta.value = cm.getValue();
    });
    return editor;
  }

  // Create editors if textareas present
  const practiceEditor = createEditor('code');
  const coachEditor = createEditor('prompt');

  // Ensure forms submit the editor contents
  const practiceForm = document.getElementById('practiceForm');
  if (practiceForm && practiceEditor) {
    practiceForm.addEventListener('submit', function() {
      // update underlying textarea (already updated on change, but ensure latest)
      document.getElementById('code').value = practiceEditor.getValue();
    });
  }

  const coachForm = document.getElementById('coachForm');
  if (coachForm && coachEditor) {
    coachForm.addEventListener('submit', function() {
      document.getElementById('prompt').value = coachEditor.getValue();
    });
  }
})();
