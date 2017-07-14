
// These tests are run by opening up the tests.html file
QUnit.test("errors should be supressed on keypress", function (assert) {
  initialize();
  $('input[name="text"]').trigger('keypress');
  assert.equal($('.has-error').is(':visible'), false);
});

QUnit.test("errors aren't hidden if there is no keypress", function (assert) {
  initialize();
  assert.equal($('.has-error').is(':visible'), true);
});